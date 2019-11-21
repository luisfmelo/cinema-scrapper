package main

import (
	"cinema-scrapper/api/controllers"
	"fmt"
	"github.com/getsentry/sentry-go"
	"github.com/gorilla/mux"
	"log"
	"net/http"
	"os"
	"time"
)

const defaultPort = "8080"


func main() {
	// Sentry's handler initialization
	sentryToken := os.Getenv("SENTRY_TOKEN")
	err := sentry.Init(sentry.ClientOptions{
		Dsn: fmt.Sprintf("https://%s@sentry.io/1829189", sentryToken),
	})
	// Since sentry emits events in the background we need to make sure they are sent before we shut down
	sentry.Flush(time.Second * 5)

	router := mux.NewRouter()
	router.HandleFunc("/api", controllers.HealthCheck).Methods("GET")
	router.HandleFunc("/api/cinemas", controllers.CreateCinema).Methods("POST")
	router.HandleFunc("/api/sessions", controllers.CreateSession).Methods("POST")
	router.HandleFunc("/api/movies", controllers.CreateMovie).Methods("POST")

	port := getPort()

	err = http.ListenAndServe(":"+port, router)
	if err != nil {
		sentry.CaptureException(err)
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
