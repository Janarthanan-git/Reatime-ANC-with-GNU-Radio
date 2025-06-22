# 🎧 Real-Time Active Noise Cancellation using GNU Radio

This project demonstrates real-time Active Noise Cancellation using an LMS adaptive filter implemented inside GNU Radio Companion (GRC) with Embedded Python Blocks.

## 📦 Features
- Real-time processing using mic input and WAV file as reference
- Custom LMS filter (Least Mean Square)
- Visual signal analysis using QT GUI Time & Frequency Sinks
- Designed for embedded/digital signal processing practice

## 📂 Files
- `ANC.grc` – GNU Radio flowgraph
- `anc_epy_block_0.py` – Custom LMS adaptive block code
- `reference_noise.wav` – Sample reference noise (if applicable)
- `README.md` – This description

## 📈 Visualization
| Signal        | What It Shows |
|---------------|----------------|
| Reference     | WAV file noise |
| Mic Input     | Voice + noise  |
| Filtered Out  | Output of LMS filter |

## 🖥️ Requirements
- GNU Radio 3.10+
- Radioconda (recommended)
- Python 3.8+
- Working mic & headphones

## 🚀 How to Run
1. Open `anc_realtime.grc` in GNU Radio
2. Make sure `reference_noise.wav` exists in the same folder
3. Connect a mic and wear headphones
4. Run the flowgraph
5. Watch filtering in real time!

## 🔗 License
MIT License
