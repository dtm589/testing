package main

import "fmt"

func main() {
	var smsSendingLimit int
	var costPerSMS float64
	var hasPermission bool
	var username string
	fmt.Printf("%v %f %v %q\n", smsSendingLimit, costPerSMS, hasPermission, username)


	accountAge := 2.6
	// create a new "accountAgeInt" here
	// it should be the result of casting "accountAge" to an integer
	accountAgeInt := int(accountAge)


	averageOpenRate, displayMessage := .23, "is the average open rate of your messages"
	fmt.Println(averageOpenRate, displayMessage)


	const premiumPlanName = "Premium Plan"
	const basicPlanName = "Basic Plan"
	fmt.Println("plan:", premiumPlanName)
	fmt.Println("plan:", basicPlanName)


	const secondsInMinute = 60
	const minutesInHour = 60
	const secondsInHour = secondsInMinute * minutesInHour
	fmt.Println("number of seconds in an hour:", secondsInHour)


	const name = "Saul Goodman"
	const openRate = 30.5
	msg := fmt.Sprintf("Hi %s, your open rate is %.1f percent\n", name, openRate)
	fmt.Print(msg)


	messageLen := 10
	maxMessageLen := 20
	fmt.Println("Trying to send a message of length:", messageLen, "and a max length of:", maxMessageLen)
	if messageLen <= maxMessageLen {
		fmt.Println("Message sent")
	} else {
		fmt.Println("Message not sent")
	}

}

func concat(s1 string, s2 string) string {
	return s1 + s2
}


func main() {
	sendsSoFar := 430
	const sendsToAdd = 25
	sendsSoFar = incrementSends(sendsSoFar, sendsToAdd)
	fmt.Println("you've sent", sendsSoFar, "messages")
}

func incrementSends(sendsSoFar, sendsToAdd int) int {
	return sendsSoFar + sendsToAdd
}


func main() {
	firstName, _ := getNames()
	fmt.Println("Welcome to Textio,", firstName)
}

func getNames() (string, string) {
	return "John", "Doe"
}


func yearsUntilEvents(age int) (yearsUntilAdult, yearsUntilDrinking, yearsUntilCarRental int) {
	yearsUntilAdult = 18 - age
	if yearsUntilAdult < 0 {
		yearsUntilAdult = 0
	}
	yearsUntilDrinking = 21 - age
	if yearsUntilDrinking < 0 {
		yearsUntilDrinking = 0
	}
	yearsUntilCarRental = 25 - age
	if yearsUntilCarRental < 0 {
		yearsUntilCarRental = 0
	}
	return
}

// struct in Go is like a dictionary in Python or a object in JavaScript
type messageToSend struct {
	message   string
	sender    user
	recipient user
}

type user struct {
	name   string
	number int
}

func canSendMessage(mToSend messageToSend) bool {
	if mToSend.sender.name != "" && mToSend.sender.number != 0 && mToSend.recipient.name != "" && mToSend.recipient.number != 0{
		return true
	}
	return false
}


//embedded structs - the parent struct inhereits the properties of the embedded struct
type sender struct {
	rateLimit int
	user
}

type user struct {
	name   string
	number int
}


type authenticationInfo struct {
	username string
	password string
}

func (authInfo authenticationInfo) getBasicAuth() string {
	return "Authorization: Basic " + authInfo.username + ":" + authInfo.password
}