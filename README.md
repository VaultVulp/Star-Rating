# Dynamic Star Rating

Generates a dynamic star rating image (SVG) using Python, which is deployed freely via Vercel.

Inspired by [![guibranco/progressbar](https://img.shields.io/badge/guibranco%2Fprogressbar-black?style=flat&logo=github)](https://github.com/guibranco/progressbar).

This service is deployed on [Vercel](https://vercel.com) and accessible via the domain [starrating-beta.vercel.app](https://starrating-beta.vercel.app).

---

## Usage

To display a star rating of 2.7, use the following URL:

`https://starrating-beta.vercel.app/2.7/`

This will generate an SVG image showing a star rating of 2.7 out of 5.

To display a star rating of 2.7 with a star size of 48 pixels, use the following URL:

`https://starrating-beta.vercel.app/2.7/?size=48`

## Examples

| Rating | Star Rating Image                                       | Markdown                                                  |
| ------ | ------------------------------------------------------- | --------------------------------------------------------- |
| 1.0    | ![Star Rating](https://starrating-beta.vercel.app/1.0/) | `![Star Rating](https://starrating-beta.vercel.app/1.0/)` |
| 2.6    | ![Star Rating](https://starrating-beta.vercel.app/2.6/) | `![Star Rating](https://starrating-beta.vercel.app/2.6/)` |
| 3.3    | ![Star Rating](https://starrating-beta.vercel.app/3.3/) | `![Star Rating](https://starrating-beta.vercel.app/3.3/)` |
| 4.0    | ![Star Rating](https://starrating-beta.vercel.app/4.0/) | `![Star Rating](https://starrating-beta.vercel.app/4.0/)` |
| 5.0    | ![Star Rating](https://starrating-beta.vercel.app/5.0/) | `![Star Rating](https://starrating-beta.vercel.app/5.0/)` |

---

## Parameters

| Parameter | Description                                   | Default Value |
| --------- | --------------------------------------------- | ------------- |
| `rating`  | The rating value to display (between 0 and 5) | 0             |
| `size`    | The size of each star in pixels               | 24            |

| Rating | Size | Star Rating Image                                               | Markdown                                                          |
| ------ | ---- | --------------------------------------------------------------- | ----------------------------------------------------------------- |
| 3.3    | 6    | ![Star Rating](https://starrating-beta.vercel.app/3.3/?size=6)  | `![Star Rating](https://starrating-beta.vercel.app/3.3/?size=6)`  |
| 3.3    | 12   | ![Star Rating](https://starrating-beta.vercel.app/3.3/?size=12) | `![Star Rating](https://starrating-beta.vercel.app/3.3/?size=12)` |
| 3.3    | 24   | ![Star Rating](https://starrating-beta.vercel.app/3.3/?size=24) | `![Star Rating](https://starrating-beta.vercel.app/3.3/?size=24)` |
| 3.3    | 32   | ![Star Rating](https://starrating-beta.vercel.app/3.3/?size=32) | `![Star Rating](https://starrating-beta.vercel.app/3.3/?size=32)` |
| 3.3    | 48   | ![Star Rating](https://starrating-beta.vercel.app/3.3/?size=48) | `![Star Rating](https://starrating-beta.vercel.app/3.3/?size=48)` |
| 3.3    | 96   | ![Star Rating](https://starrating-beta.vercel.app/3.3/?size=96) | `![Star Rating](https://starrating-beta.vercel.app/3.3/?size=96)` |


## Moon Examples

To display a moon rating of 3.5, use the following URL:

`https://starrating-beta.vercel.app/moon/3.5/`

This will generate a text representation of the moon rating of 3.5 out of 5.

| Rating | Moon Rating Image                                       | Markdown                                                  |
| ------ | ------------------------------------------------------- | --------------------------------------------------------- |
| 1.0    | 🌑🌑🌑🌑🌑 | `![Moon Rating](https://starrating-beta.vercel.app/moon/1.0/)` |
| 2.6    | 🌑🌑🌑🌑🌑 | `![Moon Rating](https://starrating-beta.vercel.app/moon/2.6/)` |
| 3.3    | 🌑🌑🌑🌑🌑 | `![Moon Rating](https://starrating-beta.vercel.app/moon/3.3/)` |
| 4.0    | 🌑🌑🌑🌑🌑 | `![Moon Rating](https://starrating-beta.vercel.app/moon/4.0/)` |
| 5.0    | 🌑🌑🌑🌑🌑 | `![Moon Rating](https://starrating-beta.vercel.app/moon/5.0/)` |
