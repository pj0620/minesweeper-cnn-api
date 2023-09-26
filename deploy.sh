#!/bin/sh

gcloud run deploy minesweeper-cnn-api \
  --region us-east1 \
  --project minesweeper-cnn \
  --platform managed \
  --source .
