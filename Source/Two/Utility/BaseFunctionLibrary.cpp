// Fill out your copyright notice in the Description page of Project Settings.


#include "BaseFunctionLibrary.h"
#include "GameFramework/PlayerState.h"

bool UBaseFunctionLibrary::SetPlayerName(APlayerState* Player, FString NewPlayerName)
{
	Player->SetPlayerName(NewPlayerName);
	return true;
}
