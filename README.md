# DXF Layer Splitter

A command-line tool to **split a DXF file into individual layer files**, optionally filtered using a **regex pattern**.


## 🔧 Features

- Split a DXF file into **separate files per layer**
- Optional **regex-based filtering** of layer names
- Output DXF files into a specified directory
- Supports all standard DXF formats (R12, R2000, R2010, etc.)


## 📦 Requirements

- Python 3.7 or newer
- Install dependencies:

```bash
pip install ezdxf click
````


## 🚀 Usage

```bash
python split.py INPUT_FILE OUTPUT_DIR [--pattern PATTERN]
```

### 📌 Arguments

| Argument          | Description                                     |
| ----------------- | ----------------------------------------------- |
| `INPUT_FILE`      | Path to the source `.dxf` file                  |
| `OUTPUT_DIR`      | Directory to save the split DXF files           |
| `--pattern`, `-p` | *(Optional)* Regex pattern to match layer names |


### 💡 Examples

#### 🔹 Export All Layers

```bash
python split.py drawing.dxf output/
```

This will export **every layer** from `drawing.dxf` into its own DXF file under `output/`.

#### 🔹 Export Only Matching Layers

```bash
python split.py drawing.dxf output/ -p "^A_"
```

This will export only layers whose names start with `A_`, e.g., `A_WALLS`, `A_DOORS`, etc.

Each file contains only the entities from its corresponding layer.


## 🧩 Notes

* Only **modelspace entities** are processed.
* The tool does not currently split block definitions or layouts.
* Layer names are used as filenames—ensure they are valid for your filesystem.


## 🛠️ License

MIT License – Use freely and modify as needed.


