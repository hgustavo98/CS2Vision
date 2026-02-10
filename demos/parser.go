package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
)

type DemoData struct {
	FileSize int64  `json:"file_size"`
	FileName string `json:"file_name"`
}

func main() {
	// Parse command-line arguments
	inputFile := flag.String("file", "", "Path to the demo file")
	flag.Parse()

	if *inputFile == "" {
		fmt.Println("Error: No file provided. Use --file=<path_to_demo>")
		return
	}

	fileInfo, err := os.Stat(*inputFile)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}

	demoData := DemoData{
		FileSize: fileInfo.Size(),
		FileName: fileInfo.Name(),
	}

	output, err := json.MarshalIndent(demoData, "", "  ")
	if err != nil {
		fmt.Printf("Error generating JSON: %v\n", err)
		return
	}

	fmt.Println(string(output))
}