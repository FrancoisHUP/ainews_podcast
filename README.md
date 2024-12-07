# AI News Podcast

This project aims to generate a complete podcast based on a newsletter feed.

## Get started 

**Pull submodule**

Once you pulled the project, you need to pull the submodule (our custom podcastfy library).

```bash
$ git submodule update --init --recursive
```

## Run the project 

**Active python virtual environnement** 

```bash
$ python -m venv .venv
```

```bash
$ source .venv/Scripts/activate
```

```bash
$ pip install -r requirements.txt
```

**Run the system**

```bash
python main.py "https://buttondown.com/ainews/rss" --date 2024-12-06
```

## References

**Podcastfy**

Github : https://github.com/souzatharsis/podcastfy

Demo : https://thatupiso-podcastfy-ai-demo.hf.space/

**Swix RSS Feed** 

Link : https://buttondown.com/ainews/rss