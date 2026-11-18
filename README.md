# streamlit-loader

A single-page Streamlit gallery of 20 animated loaders:

- **10 CSS / SVG loaders**: Aurora Ring, Gooey Blobs, Orbit, DNA Helix, Equalizer, Morph, Ripple, Infinity, Newton's Cradle, Shimmer Text. No JavaScript, no images.
- **10 Lottie loaders**: the best 10 of 40 free loading animations reviewed on [LottieFiles](https://lottiefiles.com/free-animations/loading), played with [lottie-web](https://github.com/airbnb/lottie-web). Each card credits and links its creator.

The **✦ TraceBuddy** tab shows the same 20 loaders as branded loading states for TraceBuddy: one consistent, static wordmark ("Trace" in ink, "Buddy" in violet `#6d5dfc`, WCAG-contrast on white), a short status line, and a `role="status"` region that announces "TraceBuddy is loading" to screen readers while the animation itself is hidden from them.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501. The server listens on all interfaces (`.streamlit/config.toml`), so it is also reachable from other devices on your network or tailnet at `http://<host>:8501`.

## Layout

- `app.py`: the page
- `.streamlit/config.toml`: light theme, static file serving
- `static/lottie.min.js`: lottie-web 5.12.2 (MIT)
- `static/lottie/*.json`: the Lottie animations, with credits in `static/lottie/index.json`

Lottie animations are free animations from LottieFiles and remain under the [Lottie Simple License](https://lottiefiles.com/page/license) of their creators.
