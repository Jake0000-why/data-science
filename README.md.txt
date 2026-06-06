# Global Fish Species Image Dataset (iNaturalist)

## Overview
A curated fish image dataset created from iNaturalist Research Grade observations.
Organized as ML-ready species folders with metadata CSV.

## Dataset Contents
- /inat_fish_dataset/  -> species folders containing images
- /inat_meta/all_downloaded_images.csv -> metadata with license and URLs

## Use Cases
- Fish species classification
- Fish photo retrieval (CLIP embeddings)
- Training multimodal chatbot (RAG with taxonomic + habitat info)

## License
Each image retains its original iNaturalist license.
Please refer to metadata CSV for license_code and source_url.

## Data Source
https://api.inaturalist.org/v1/docs/
