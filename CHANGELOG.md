### Install

To install the latest version of gif run:

```
pip install -U gif
```


### Changelog

---

#### 4.0 (2022-05-10)

- Removed: Altair support
- Removed: Plotly support
- Bumped: Upstream dependencies
- Tests: Simplified pytest suite

#### 3.0.0 (2020-09-10)

- Feature: Plotly support! (Thanks @alanrivetta for the suggestion!)
- Feature: seconds/milliseconds unit support in `gif.save`
- Feature: between {"frames", "startend"} support in `gif.save`
- Feature: **kwargs export/save support in `gif.options.<ploting_library>` (Thanks @oaio for the PR!)
- Feature: added loop=True argument to `gif.save` (Thanks for the suggestion @davidwych & @sara-02!)
- Moved: matplotlib dependency is now exclusively in `pip install "gif[matplotlib]"`
- Documentation: New "love" example (Thanks @huang-sh for the PR!)
- Security: Bumped pillow dependency to >=7.1.2
