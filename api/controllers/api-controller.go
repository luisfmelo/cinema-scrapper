package controllers

import (
	"cinema-scrapper/api/responses"
	"net/http"
)

func HealthCheck(w http.ResponseWriter, r *http.Request) {
	responses.JSON(w, http.StatusOK, map[string]interface{}{"status": "alive"})
}
