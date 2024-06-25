# Making Dashboards with Maps Using Streamlit - June 26, 2024

### Data Sources

* [Washington State Hikes](https://github.com/yoshiohasegawa/wta-scraper)

### To run the dashboard locally

* If you are familiar with [GitHub](http://www.github.com), fork (if you wish) and clone this repository. If not, download the repository and unzip to a working directory. Take note of where you put it!

* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for your operating system. Please choose the latest Python 3.x version.

* You should now have access to an Anaconda command prompt, open it like you would any program. Note that you should see `(base)` somewhere in your prompt. This means you're in the base Conda environment, which we will now change. 

Navigate to the directory containing requirements.txt (included in the repo).

```bash
cd [location where the repo is saved]/cugos_streamlit
```

* Create environment.

```bash
conda create --name streamlitenv
conda activate streamlitenv
```
* Install packages.

```bash
conda install streamlitenv
conda install pandas
conda install altair
```

* Run the dashboard
```bash
streamlit run streamlit_hikes.py
```