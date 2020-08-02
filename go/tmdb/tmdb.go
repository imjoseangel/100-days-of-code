package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {

	var apikey = os.Getenv("TMDB_API")

	response, err := http.Get("https://api.themoviedb.org/3/discover/movie?api_key=" + apikey + "&primary_release_year=2017&sort_by=revenue.desc") // pragma: allowlist secret

	if err != nil {
		fmt.Printf("The HTTP request failed with error %s\n", err)
	} else {
		data, _ := ioutil.ReadAll(response.Body)
		fmt.Println(string(data))
	}

}
