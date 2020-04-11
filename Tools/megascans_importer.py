

import sys, json, asyncio

host, port = 'localhost',24981  # The port number here is just an arbitrary number that's > 20000

def add_to_manifest(asset_id):
    print(asset_id)
    try:
            with open("../megascans_ids.txt", 'a') as f, open("../megascans_ids.txt", 'r') as c:
                
                    contents = c.read()
                    if asset_id not in contents:
                            f.write(f"{asset_id}\n")
    except Exception as e:
            with open("../megascans_ids.txt", 'w') as f:
                    f.write(f"{asset_id}\n")
            print(e)

#Example method that reads the asset id and try to find the albedo map and print it's path to console.
def ms_read_data (imported_assets_array):
    #Now you can send or use the data as you like.
    for asset in imported_assets_array:
            assetId = asset['AssetID']
            add_to_manifest(assetId)
            print ("Imported asset ID is: %s" %(assetId))
            #Example to look for albedo map and then printing out it's path.
            for item in asset['TextureList']:
                    if item[1] == "albedo": #Matching the type of texture.
                            print("Albedo path is: %s" %(item[0]))
                            break

def ms_asset_importer (imported_data): 
    print ("Imported json data")
    try:
        #Array of assets in case of Batch export.
        imported_assets_array = []
        #Parsing JSON data that we received earlier.
        json_array = json.loads(imported_data)

        #For each asset data in the received array of assets (Multiple in case of batch export)
        for jData in json_array:
                #print(jdata)
                packed_textures_list = [] #Channel packed texture list
                textures_list = [] #All of the other textures list.
                geo_list = [] #Geometry list will contain data about meshes and LODs.

                #Get and store textures in the textures_list.
                for item in jData['components']:
                        if 'path' in item:
                                textures_list.append([item['path'], item['type']])
                
                #Get and store the geometry in the geo_list.
                for item in jData['meshList']:
                        if 'path' in item:
                                geo_list.append(item['path'])
                
                #Get and store the channel packed textures in the packed_texture_list.
                for item in jData['packedTextures']:
                        if 'path' in item:
                                packed_textures_list.append([item['path'], item['type']])

                #Reading other variables from JSON data. 
                export_ = dict({
                        "AssetID": jData['id'],
                        "FolderPath": jData['path'],
                        "MeshList": geo_list,
                        "TextureList": textures_list,
                        "packedTextures": packed_textures_list,
                        "Resolution": jData['resolution'],
                        "activeLOD": jData['activeLOD']
                })
                
                #Append the filtered data to imported assets array.
                imported_assets_array.append(export_)

        #Calling the example method.
        ms_read_data(imported_assets_array)

    #Exception handling.
    except Exception as e:
            print('Error Line : {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            pass

#Calling this method with stop the async server. 
def stop_server():
    try:
        for task in asyncio.Task.all_tasks():
            task.cancel()
    except:
        pass

# cleanup previous tasks
for task in asyncio.Task.all_tasks():
    task.cancel()

async def bridgeLiveLink (reader, writer):
    #Keep listening to the port indefinitely.
    while True:
    #Data buffer size
        buffer_size = 4096*2
        #Wait for the connection and data transfer.
        data = await reader.read(buffer_size)
        if not data:
            break
        
        #If some data was received then pass it ot the importer.
        if len(data) > 0:
           
            ms_asset_importer (data.decode())

#This method has to be 'async' in order to work.
async def ms_Init():
	#Start the server.
    server = await asyncio.start_server(bridgeLiveLink, host, port)
	#Keep the server running forever.
    await server.serve_forever()

#Start main method.
asyncio.run(ms_Init())
