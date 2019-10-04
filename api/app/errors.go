package app

import (
	u "cinema-scrapper/api/utils"
	"net/http"
)

func NotFoundHandler (next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNotFound)
		u.Respond(w, u.Message(false, "This resources was not found on our server"))
		next.ServeHTTP(w, r)
	})
}