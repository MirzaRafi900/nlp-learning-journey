# Named Entity Recognition

## Overview

This project extracts important entities from news articles
using spaCy.

## Features

- Detect Persons
- Detect Organizations
- Detect Locations
- Detect Dates

## Example

Input:
Mirza Group of Industries has launched new ATGM at 30th August 2026. It's presented by major Shakhawat Al Jabeer.

Output:
______________________________
🔹 Text: Mirza Group of Industries
🏷️ Text: ORG
______________________________
🔹 Text: ATGM
🏷️ Text: ORG
______________________________
🔹 Text: 30th August 2026
🏷️ Text: DATE
______________________________
🔹 Text: Shakhawat Al Jabeer
🏷️ Text: PERSON
______________________________
