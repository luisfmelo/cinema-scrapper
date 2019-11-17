package models

import (
	"errors"
	"github.com/jinzhu/gorm"
	"time"
)

type Session struct {
	gorm.Model

	MovieID   uint      `json:"-" gorm:"foreignkey:ID,not null"`
	Movie     Movie     `json:"movie"`
	CinemaID  uint      `json:"-" gorm:"foreignkey:ID,not null"`
	Cinema    Cinema    `json:"cinema"`
	Room      string    `json:"room"`
	StartTime time.Time `json:"start_time"`
}

func SaveSession(session *Session) error {

	// Create Cinema if does not exist
	err := SaveCinema(&session.Cinema)
	if err != nil {
		return err
	}

	// Create Movie if does not exist
	err = SaveMovie(&session.Movie)
	if err != nil {
		return err
	}

	// Create Session
	db := db.Where(Session{MovieID: session.Movie.ID, CinemaID: session.Cinema.ID, Room: session.Room, StartTime: session.StartTime}).
		FirstOrCreate(&session)
	if db.Error != nil {
		return errors.New("failed to create a cinema. " + db.Error.Error())
	}

	if session.ID <= 0 {
		return errors.New("failed to create a cinema, connection error")
	}

	return nil
}
