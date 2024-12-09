# AI News Podcast

This project aims to generate a complete podcast based on a newsletter feed.

## Get started 

### Setup project

**Pull submodule**

Once you pulled the project, you need to pull the submodule (our custom podcastfy library).

```bash
git submodule update --init --recursive
```

> **_NOTE:_**  You can pull the main project plus the submodule ```git pull --recurse-submodules``` or automaticly pull submodules with ```git config submodule.recurse true``` 

**Install uv cli** 
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Create venv**
```bash
uv sync
```

**Activate venv**
```bash
source .venv/bin/activate
```

**Setup keys**

Set your [ElevenLabs api key](https://elevenlabs.io/app/settings/api-keys) in ```.env``` file   

```
.
├── data/
├── output/
├── ...
├── .env
├── main.py
```

Content of ```.env``` file   

```
ELEVENLABS_KEY=sk_...
```

### Run the project 

**Run the system**

```bash
python main.py "https://buttondown.com/ainews/rss" --date 2024-12-06
```



## Run tests

```bash
pytest tests/test_clean_rss_item.py -v
```



## References

**Podcastfy**

Github : https://github.com/souzatharsis/podcastfy

Demo : https://thatupiso-podcastfy-ai-demo.hf.space/

**Swix RSS Feed** 

Link : https://buttondown.com/ainews/rss
