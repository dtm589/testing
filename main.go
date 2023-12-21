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