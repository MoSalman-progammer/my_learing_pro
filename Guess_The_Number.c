/*

This is a simple guess the number game.
You have to guess a random number between x and y in a attempt.

*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<ctype.h>

int main(){
    
    // Range.
    int upper_end = 100;
    int lower_end = 0;

    // Attempt.
    int number_of_attempt = 6;
    
    // The random number. Initially set to zero before generating one
    int random_number = 0;
    
    // The number guessed by the Player.
    int guessed_number = 0;

    // Play again response.
    char play_again_response;

    printf("Welcome to Guess the number game.\nyou have %d attempts.\n",number_of_attempt);
    
    //Game start.
    game:
    
    // Seed the rand function with current time. To generate random number
    srand(time(0));
    
    //set the random number.
    random_number = lower_end + rand()%(upper_end - lower_end + 1);
    
    for ( int round = 1; round <= number_of_attempt; round++)
    {
       printf("Guess the number.\n");
       scanf("%d", &guessed_number);
       if (guessed_number == random_number)
       {
        printf("Conratulation You found the right number in %d Attempt.\n",round);
        break;
       }
       else if (guessed_number > random_number)
       {
        printf("Guess lower.\n");
       }
       else
       {
        printf("Guess higher.\n");
       }
    }

    if (guessed_number!=random_number)
    {
        printf("The correct number was %D.\n",random_number);
    }
    
    printf("Game Over.\n");
    
    //asking player if they want to play again
    printf("Do you want to play again. Enter y/n.\n");
    scanf(" %c", &play_again_response);
    play_again_response = tolower(play_again_response);

    if (play_again_response == 'y')
    {
        goto game;
    }
    
    return 0;
}