// Aiden. S (SquarerFive). 2020. 

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "BaseFunctionLibrary.generated.h"

class APlayerState;
/**
 * 
 */
UCLASS()
class TWO_API UBaseFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
public:
		UFUNCTION(BlueprintCallable, Category="Redux Project")
		static bool SetPlayerName(APlayerState* Player, FString NewName);
};
