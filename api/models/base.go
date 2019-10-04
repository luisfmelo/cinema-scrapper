package models

import (
	"cinema-scrapper/api/old_stuff"
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"github.com/joho/godotenv"
	"log"
	"os"
)

var db *gorm.DB

func init() {

	mode := os.Getenv("mode")

	err := godotenv.Load()
	if err != nil {
		log.Println("Failed to loading environment variables")
		panic(err)
	}

	username := os.Getenv("db_user")
	password := os.Getenv("db_pass")
	dbName := os.Getenv("db_name")
	dbHost := os.Getenv("db_host")
	dbPort := os.Getenv("db_port")

	dbUri := fmt.Sprintf("host=%s port=%s user=%s dbname=%s sslmode=disable password=%s", dbHost, dbPort, username, dbName, password)

	db, err := gorm.Open("postgres", dbUri)
	if err != nil {
		log.Println("Failed to connect to database")
		panic(err)
	}
	log.Println("Database connected")

	if mode != "PROD"{
		db = db.Debug()
	}

	db.AutoMigrate(&old_stuff.Account{}, &old_stuff.Contact{})
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
