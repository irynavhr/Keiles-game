// Developed by Iryna Hrytsenko

package main

import (
	"fmt"
	"math/rand"
	"time"
)

var (
	matchesExisting = []int{1, 1, 1, 1, 1, 1, 1, 1, 1} // Example with 10 matches
	choiceList      []int
	choiceQuantity  = 0
	errorr          = false

	c       = "with computer"
	p       = "with another player"
	gameMod = c // Or p

	Player          = "Player"
	Computer        = "Computer"
	Player1         = "Player1"
	Player2         = "Player2"
	currentPlayTurn = "Player" // Or "Computer" if ComputerMod AND "Player1" or "Player2" in playersMod
)

func printMatches() {
	fmt.Println("\nMatches:")
	for _, match := range matchesExisting {
		if match == 1 {
			fmt.Print(" | ")
		} else {
			fmt.Print(" _ ")
		}
	}
	fmt.Println("\n ")
}

func printError(msg string) {
	fmt.Println("\nError:", msg, "\nTry once more:")
	printMatches()
}

func playerInputProcessing(who string) {
	choiceList = []int{}
	var matchID int
	errorr = false
	// вибираємо скільки сірників
	fmt.Print("enter the number of matches tou wanna take - 1 or 2: \n")
	fmt.Scan(&choiceQuantity)
	// і який номер першого з них
	fmt.Print("enter the (first)match number to take 1-(8)9: \n")
	fmt.Scan(&matchID)
	matchID-- // перетворюємо номер на індекс
	// якщо виключення - ерор
	if (matchID < 0) || (choiceQuantity != 1 && choiceQuantity != 2) || (choiceQuantity == 2 && matchID >= len(matchesExisting)-1) || (matchID >= len(matchesExisting)) || (matchesExisting[matchID] == 0) {
		printError("Invalid match number or quantity of matches already taken.")
		errorr = true
	} else if choiceQuantity == 2 && matchesExisting[matchID+1] == 0 {
		printError("Invalid match number or quantity of matches already taken.")
		errorr = true
	} else { // інакше - видаляємо сірники
		choiceList = append(choiceList, matchID)
		matchesExisting[matchID] = 0
		if choiceQuantity == 2 {
			choiceList = append(choiceList, matchID+1)
			matchesExisting[matchID+1] = 0
		}
		printMatches()
		currentPlayTurn = who
	}
}

func ComputerMakeTurn() {
	choiceList = []int{}
	mixedIDList := rand.Perm(len(matchesExisting) - 1)
	// вибираємо 2 якщо можна
	for _, i := range mixedIDList {
		if matchesExisting[i] == 1 && matchesExisting[i+1] == 1 {
			choiceList = append(choiceList, i)
			choiceList = append(choiceList, i+1)
			matchesExisting[i] = 0
			matchesExisting[i+1] = 0
			break
		}
	}
	// інакше вибираємо 1
	mixedIDList = rand.Perm(len(matchesExisting))
	if len(choiceList) == 0 {
		for _, i := range mixedIDList {
			if matchesExisting[i] == 1 {
				choiceList = append(choiceList, i)
				matchesExisting[i] = 0
				break
			}
		}
	}
	printMatches()
}

func checkWin(who string) bool {
	if sumMatches() == 0 {
		fmt.Println(who, "wins!")
		return true
	}
	return false
}

func sumMatches() int {
	sum := 0
	for _, match := range matchesExisting {
		sum += match
	}
	return sum
}

func main() {
	var typedM string
	fmt.Println("_KEILES GAME_\nThe matches are placed in one row. \nTwo players take turns taking 1 match or 2 neighboring ones from the row. \nWhoever takes the last match wins.")
	// вибираємо режим гри
	fmt.Println("\nChoose mod, please:\nTap 'c' if with computer\nAnd 'p' if with another player")
	fmt.Scan(&typedM)
	for {
		if typedM == "p" || typedM == "c" {
			break
		}
		fmt.Println("Uncorrect mod! Try once more time:")
		fmt.Scan(&typedM)
	}
	if typedM == "p" {
		gameMod = p
		currentPlayTurn = Player1
	} else if typedM == "c" {
		gameMod = c
		currentPlayTurn = Player
	}
	// відображаємо режим та сірники
	fmt.Println("GameMod: ", gameMod)
	printMatches()
	// обробка подій
	for {
		if gameMod == c {
			if currentPlayTurn == Player {
				if errorr != true {
					fmt.Println(currentPlayTurn, "turn:")
				}
				playerInputProcessing(Computer)
				if checkWin(Player) {
					break
				}
			} else if currentPlayTurn == Computer {
				fmt.Println(Computer, "turn...")
				ComputerMakeTurn()
				time.Sleep(1 * time.Second)
				if checkWin(Computer) {
					break
				}
				currentPlayTurn = Player
			}
		} else if gameMod == p {
			if currentPlayTurn == Player1 {
				if errorr != true {
					fmt.Println(currentPlayTurn, "turn:")
				}
				playerInputProcessing(Player2)
				if checkWin(Player1) {
					break
				}
			} else if currentPlayTurn == Player2 {
				if errorr != true {
					fmt.Println(currentPlayTurn, "turn:")
				}
				playerInputProcessing(Player1)
				if checkWin(Player2) {
					break
				}
			}
		}
	}
}
