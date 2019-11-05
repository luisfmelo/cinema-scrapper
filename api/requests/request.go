package requests

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
)

func ParseRequest(r *http.Request, obj interface{}) error {
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		return err
	}
	return json.Unmarshal(body, &obj)
}
