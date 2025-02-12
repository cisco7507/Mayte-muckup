# Functional Specification Document for Creative Management Modules

**Version:** 1.3  
**Date:** February 12, 2025  
**Author:** [Your Name]

---

## 1. Introduction

### 1.1 Purpose

This document specifies the functional requirements, user workflows, and system behaviors for two key functions of the website:

1. **Outside Creative** – Allows users to upload creative media files (MP4/MOV), enter associated metadata, and initiate a transcoding process.
2. **Broadcast File Creative** – Enables users to search for creative assets (from an internal database) by advertiser and select individual creative records for further processing.

### 1.2 Scope

This document covers the following functionality:

- **Outside Creative:**
  - **File Upload:**
    - Accepts MP4 or MOV files.
    - File type is validated immediately upon selection.
    - A unique UUID is generated immediately upon a valid file upload and displayed.
  - **Metadata Entry Form:**  
    The metadata form includes:
    - **Title:** A free-text input field.
    - **Language:** A dropdown with two options (“English” or “French”).
    - **Duration:** A dropdown for duration intervals with options: 5, 10, 15, 30, or 60 seconds.
    - **Advertise:** A searchable text field with dynamic suggestions (populated from an internal data source).
    - **Server Endpoint:** A multi-select field with options: FW, Cadent, GAM, Reogers, Telus, ALL.
    - **Industry:** A dropdown with options “Cadent” and “FW.”
    - **Sub-Industry:** A dynamic, searchable field that appears if the selected Industry is either “Cadent” or “FW.”
    - **Content Type:** Radio buttons with options “VOD” or “Linear.”
  - **Processing:**  
    On submission, the file and metadata (including the pre-generated UUID) are stored, and a vantage transcode process is initiated. A confirmation message is then displayed.

- **Broadcast File Creative:**
  - **Advertiser Search:**
    - A searchable Advertiser field with dynamic suggestions is provided.
    - The user enters an advertiser name, and the system queries an internal IBMS creative data source to return matching creative records.
  - **Search Results Table:**  
    The search results are displayed in a table with the following columns:
    - HouseId
    - Title
    - Duration
    - Product
    - ISCI  
    Each row also includes:
    - A checkbox for selection.
    - An individual Industry dropdown (with options “Cadent” and “FW”) for specifying the industry for that row.
    - A dynamic, searchable Sub-Industry field (that appears when the Industry is set to “Cadent” or “FW”).
  - **Global Processing Options:**  
    A global Server Endpoint multi-select field is provided.
  - **Processing:**  
    The user selects one or more creative rows, sets the per-row Industry/Sub-Industry values, and clicks a “Process Selected Creative” button. A confirmation message displays the selected server endpoints and details (HouseId, per-row Industry, and Sub-Industry) for the processed items.

### 1.3 Intended Audience

- Front-end and Back-end Developers  
- QA/Testers  
- Project Managers  
- Stakeholders

---

## 2. Functional Overview

This section provides a high-level overview of the user workflows for each function.

### 2.1 Outside Creative

1. **File Upload:**  
   - The user selects a file (only MP4 or MOV are allowed).
   - The system validates the file type immediately.
2. **UUID Generation:**  
   - Upon successful file validation, a unique UUID is generated and displayed on the subsequent metadata form.
3. **Metadata Entry:**  
   - The user enters the creative metadata:
     - **Title:** Free-text input.
     - **Language:** Select either “English” or “French.”
     - **Duration:** Select a duration interval (5, 10, 15, 30, or 60 seconds).
     - **Advertise:** Use a searchable input with dynamic suggestions.
     - **Server Endpoint:** Choose one or more endpoints from a multi-select field.
     - **Industry:** Select “Cadent” or “FW.”
     - **Sub-Industry:** A dynamic searchable field appears if the Industry is “Cadent” or “FW.”
     - **Content Type:** Choose between “VOD” and “Linear.”
4. **Submission & Processing:**  
   - On submission, the file and metadata (including the UUID) are stored, and a vantage transcode process is initiated.
5. **Feedback:**  
   - A confirmation message is displayed showing key details (including the UUID, Title, Language, Duration, Server Endpoints) and indicating that the transcoding process has started.

### 2.2 Broadcast File Creative

1. **Advertiser Search:**  
   - The user enters an advertiser name into a searchable field that provides dynamic suggestions.
   - Upon clicking the search button, the system queries the internal IBMS creative data source for creative records associated with the selected advertiser.
2. **Search Results Display:**  
   - The results are displayed in a table with columns for HouseId, Title, Duration, Product, and ISCI.
   - Each row includes a checkbox for selection.
   - Each row also provides an individual Industry dropdown (with options “Cadent” and “FW”) and, if applicable, a dynamic searchable Sub-Industry field.
3. **Processing Options:**  
   - A global Server Endpoint multi-select field is provided.
   - The user selects one or more creative rows (using checkboxes) and sets the per-row Industry/Sub-Industry values.
4. **Submission & Processing:**  
   - Upon clicking the “Process Selected Creative” button, the system collects the selected creative rows along with the global processing options.
5. **Feedback:**  
   - A confirmation message is displayed, indicating the selected Server Endpoints and details for each processed creative (HouseId, Industry, and Sub-Industry, if applicable).

---

## 3. Functional Requirements

### 3.1 Outside Creative Function

#### 3.1.1 File Upload & UUID Generation
- **FR1.1:** The system shall allow users to upload files with only MP4 or MOV extensions.
- **FR1.2:** The file type shall be validated immediately upon selection.
- **FR1.3:** If the file format is invalid, an error message is displayed.
- **FR1.4:** Upon a valid file upload, the system shall generate a unique UUID immediately and display it (read-only) in the metadata form.

#### 3.1.2 Metadata Collection
- **FR1.5:** The metadata form shall include the following fields:
  - **Title:** A free-text input.
  - **Language:** A dropdown with options “English” and “French.”
  - **Duration:** A dropdown with fixed intervals (5, 10, 15, 30, 60 seconds).
  - **Advertise:** A searchable text input that displays dynamic suggestions based on an internal advertiser data source.
  - **Server Endpoint:** A multi-select field with options: FW, Cadent, GAM, Reogers, Telus, ALL.
  - **Industry:** A dropdown with options “Cadent” and “FW.”
  - **Sub-Industry:** A dynamic, searchable input field that appears if the Industry is set to “Cadent” or “FW.” The suggestions are filtered based on the selected Industry.
  - **Content Type:** Radio buttons with options “VOD” and “Linear.”

#### 3.1.3 Submission & Processing
- **FR1.6:** Upon submission, the system shall store the file and all metadata (including the pre-generated UUID).
- **FR1.7:** The system shall then trigger a vantage transcode process.
- **FR1.8:** A confirmation message shall be displayed that includes:
  - The generated UUID.
  - Entered Title, Language, Duration, and selected Server Endpoints.
  - A note indicating that the transcoding process has been initiated.

### 3.2 Broadcast File Creative Function

#### 3.2.1 Advertiser Search and Results
- **FR2.1:** The system shall provide a searchable field for the advertiser. As the user types, dynamic suggestions are displayed.
- **FR2.2:** When the user initiates a search, the system shall query the internal IBMS creative data source for all creative records associated with the entered advertiser.
- **FR2.3:** The search results shall be displayed in a table that includes the following columns for each creative record:
  - HouseId
  - Title
  - Duration
  - Product
  - ISCI
- **FR2.4:** Each row shall include a checkbox for selection.

#### 3.2.2 Per-Row Processing Options
- **FR2.5:** For each creative record in the search results, an individual Industry dropdown shall be provided with options “Cadent” and “FW.”
- **FR2.6:** If the user selects “Cadent” or “FW” in the per-row Industry dropdown, a dynamic, searchable Sub-Industry field shall appear for that row.
- **FR2.7:** The per-row Industry and Sub-Industry values shall be recorded when the creative is processed.

#### 3.2.3 Global Processing Options and Submission
- **FR2.8:** A global Server Endpoint multi-select field shall be provided (with options: FW, Cadent, GAM, Reogers, Telus, ALL).
- **FR2.9:** The user shall be able to select one or more creative rows (using the checkboxes) and specify per-row Industry/Sub-Industry values.
- **FR2.10:** When the “Process Selected Creative” button is clicked, the system shall collect:
  - The globally selected Server Endpoint values.
  - The details (HouseId, per-row Industry, and Sub-Industry) for each selected creative.
- **FR2.11:** The system shall display a confirmation message showing:
  - The selected Server Endpoints.
  - A summary of each processed creative (HouseId, Industry, and Sub-Industry).

---

## 4. Non-Functional Requirements

### 4.1 Performance
- **NFR1:** The file upload and metadata forms shall load responsively.
- **NFR2:** Dynamic suggestions (for Advertise and Sub-Industry fields) shall update in real time as the user types.

### 4.2 Security
- **NFR3:** All file uploads and user inputs must be validated and sanitized to prevent security vulnerabilities.
- **NFR4:** Data entered in the metadata and search forms must be validated to prevent injection and other common attacks.

### 4.3 Usability
- **NFR5:** The user interface must be intuitive and provide clear instructions and error messages.
- **NFR6:** Dynamic elements such as searchable fields and multi-select lists must be easy to use and responsive.

### 4.4 Error Handling & Logging
- **NFR7:** The system shall provide clear, user-friendly error messages for file upload failures, input validation errors, or processing errors.
- **NFR8:** All user actions and system events (such as file upload, metadata submission, and creative processing) shall be logged for audit and troubleshooting purposes.

---

## 5. Data Models & Database Schematics

### 5.1 Data Sources

- **Advertiser Data Source:**  
  - Contains the available options for the searchable Advertise field and advertiser search suggestions.
  
- **Creative Request Data Store (for Outside Creative):**  
  - Data items include:
    - `uuid` (unique identifier)
    - `file_path`
    - `title`
    - `language`
    - `duration`
    - `advertise`
    - `server_endpoint` (one or more values)
    - `industry`
    - `sub_industry` (if applicable)
    - `content_type`
    - `created_at`

- **IBMS Creative Data Source (for Broadcast File Creative):**  
  - Data items include:
    - `houseId`
    - `title`
    - `duration`
    - `product`
    - `isci`
    - `advertiser` (used for search matching)

- **Sub-Industry Data Source:**  
  - Contains sub-industry options mapped to each Industry (e.g., for “FW” and “Cadent”).

---

## 6. User Workflow Diagrams

### 6.1 Outside Creative Workflow

```plaintext
[User]
   │
   ├─> Upload File (MP4/MOV)
   │      │
   │      └─> Validate File Type
   │             │
   │             └─> Generate UUID Immediately
   │                        │
   │                        └─> Display UUID on Metadata Form
   │                                    │
   │                                    └─> Enter Metadata:
   │                                             - Title (free text)
   │                                             - Language (English/French)
   │                                             - Duration (5, 10, 15, 30, 60 seconds)
   │                                             - Advertise (searchable)
   │                                             - Server Endpoint (multi-select)
   │                                             - Industry (Cadent or FW)
   │                                             - [Dynamic] Sub-Industry (if applicable)
   │                                             - Content Type (VOD/Linear)
   │
   └─> Submit Metadata
           │
           └─> Save File & Metadata
                   │
                   └─> Trigger Vantage Transcode Process
                           │
                           └─> Display Confirmation Message 
                               (includes UUID, Title, Language, Duration, Server Endpoints, etc.)
```

```plaintext
[User]
   │
   ├─> Enter Advertiser in Search Field (searchable with suggestions)
   │      │
   │      └─> Initiate Search → System queries IBMS Creative Data Source
   │                  │
   │                  └─> Display Search Results in Table:
   │                             - Columns: HouseId, Title, Duration, Product, ISCI
   │                             - Each row includes:
   │                                   * Checkbox for selection
   │                                   * Individual Industry dropdown (Cadent/FW)
   │                                   * [Dynamic] Sub-Industry input (if applicable)
   │
   ├─> Select one or more creative rows (via checkboxes)
   │
   ├─> Set Global Processing Options:
   │         - Server Endpoint (multi-select)
   │
   └─> Click "Process Selected Creative"
           │
           └─> System collects selected rows and per-row Industry/Sub-Industry values,
                   plus global Server Endpoint selections
                           │
                           └─> Display Confirmation Message with:
                                   - Selected Server Endpoints
                                   - Summary of Processed Creative (HouseId, per-row Industry, Sub-Industry)
```