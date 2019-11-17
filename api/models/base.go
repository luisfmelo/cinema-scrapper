package models

import (
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"log"
	"os"
)

var db *gorm.DB

func init() {

	mode, ok := os.LookupEnv("mode")
	if !ok {
		mode = "DEBUG"
	}

	username := os.Getenv("POSTGRES_USER")
	password := os.Getenv("POSTGRES_PASSWORD")
	dbName := os.Getenv("POSTGRES_DB")
	dbHost, ok := os.LookupEnv("POSTGRES_HOST")
	if !ok {
		dbHost = "db"
	}
	dbPort, ok := os.LookupEnv("POSTGRES_PORT")
	if !ok {
		dbPort = "5432"
	}

	dbUri := fmt.Sprintf("host=%s port=%s user=%s dbname=%s sslmode=disable password=%s", dbHost, dbPort, username, dbName, password)

	conn, err := gorm.Open("postgres", dbUri)
	if err != nil {
		log.Println("Failed to connect to database")
		panic(err)
	}
	log.Println("Database connected")

	if mode != "PROD" {
		conn = conn.Debug()
	}

	db = conn.AutoMigrate(&Cinema{}, &Movie{}, &Session{})
	db.Model(&Session{}).AddUniqueIndex("idx_session", "movie_id", "cinema_id", "room", "start_time")
	db.Model(&Cinema{}).AddUniqueIndex("idx_cinema", "name", "city", "company")
}

func GetDB() *gorm.DB {
	return db
}

func CloseDB() {
	err := db.Close()
	if err != nil {
		log.Println("Error while closing database")
	}
	log.Println("Database closed")
}
