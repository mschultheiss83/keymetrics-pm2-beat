package main

import (
	"os"

	"github.com/elastic/beats/libbeat/beat"

	"github.com/mschultheiss83/keymetrics-pm2-beat/beater"
)

func main() {
	err := beat.Run("keymetrics-pm2-beat", "", beater.New)
	if err != nil {
		os.Exit(1)
	}
}
