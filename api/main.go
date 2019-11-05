package main

import (
	"cinema-scrapper/api/controllers"
	"cinema-scrapper/api/responses"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"os"
)

const defaultPort = "8080"

func main() {
	router := mux.NewRouter()

	router.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
		responses.JSON(w, http.StatusOK, map[string]interface{}{"status": "alive"})
	}).Methods("GET")
	router.HandleFunc("/api/cinemas", controllers.CreateCinema).Methods("POST")
	router.HandleFunc("/api/sessions", controllers.CreateSession).Methods("POST")
	router.HandleFunc("/api/movies", controllers.CreateMovie).Methods("POST")

	port := getPort()

	err := http.ListenAndServe(":"+port, router)
	if err != nil {
		log.Fatal("Error starting the server. " + err.Error())
	}

}

func getPort() string {
	port := os.Getenv("PORT")
	if port != "" {
		return port
	}
	return defaultPort
}
