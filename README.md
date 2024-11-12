# Dynamic Star Rating

Generates a dynamic star rating image (SVG) using Python, which is deployed freely via Vercel.

![Star Rating](https://starrating-beta.vercel.app/1.0/) ![Star Rating](https://starrating-beta.vercel.app/3.5/) ![Star Rating](https://starrating-beta.vercel.app/5.0/)

Inspired by [![guibranco/progressbar](https://img.shields.io/badge/guibranco%2Fprogressbar-black?style=flat&logo=github)](https://github.com/guibranco/progressbar).

---

## Usage

This service is deployed on [Vercel](https://vercel.com) and accessible via the domain [starrating-beta.vercel.app](https://starrating-beta.vercel.app).

---

## Parameters

| Parameter | Description                                   | Default Value |
| --------- | --------------------------------------------- | ------------- |
| `rating`  | The rating value to display (between 0 and 5) | 0             |
| `size`    | The size of each star in pixels               | 24            |

---

## Example

To display a star rating of 2.7, use the following URL:

`https://starrating-beta.vercel.app/2.7/`

This will generate an SVG image showing a star rating of 2.7 out of 5.

To display a star rating of 2.7 with a star size of 48 pixels, use the following URL:

`https://starrating-beta.vercel.app/2.7/?size=48`
