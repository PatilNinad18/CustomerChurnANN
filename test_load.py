import tensorflow as tf
import h5py

# --- 1. Try loading without compiling
try:
    model = tf.keras.models.load_model("model.h5", compile=False)
    print("✅ Model loaded successfully")
except Exception as e:
    print("❌ Error while loading:", e)

# --- 2. Inspect h5 file contents
with h5py.File("model.h5", "r") as f:
    print("Contents of model.h5:", list(f.keys()))
