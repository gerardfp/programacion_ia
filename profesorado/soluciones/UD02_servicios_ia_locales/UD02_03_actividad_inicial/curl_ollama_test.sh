#!/bin/bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:3b",
  "prompt": "¿Por qué usar inferencia local?",
  "stream": false
}'
