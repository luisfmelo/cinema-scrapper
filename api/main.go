package main

import (
	"cinema-scrapper/api/controllers"
	"cinema-scrapper/api/old_stuff"
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
	"os"
)

func main() {

	router := mux.NewRouter()

	router.HandleFunc("/api/sessions", controllers.CreateSession).Methods("POST")

	port := os.Getenv("PORT")
	if port == "" {
		port = "8000" //localhost
	}

	err := http.ListenAndServe(":"+port, router)
	if err != nil {
		fmt.Print(err)
	}
}