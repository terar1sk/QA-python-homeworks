# ============================================================
#  Dockerfile — python-automation-QA + Allure
# ============================================================
FROM python:3.11-slim

WORKDIR /app

# ── System dependencies ──────────────────────────────────────
# openjdk-21 is required to run the Allure CLI
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
        libjpeg-dev \
        zlib1g-dev \
        # openjdk-17 is not available on Debian trixie, use openjdk-21al
    openjdk-21-jre-headless \
        curl \
        unzip \
    && rm -rf /var/lib/apt/lists/*

# ── Install Allure CLI ───────────────────────────────────────
RUN curl -sLo /tmp/allure.zip \
        https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.zip \
    && unzip -q /tmp/allure.zip -d /opt \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/local/bin/allure \
    && rm /tmp/allure.zip

# ── Python dependencies ──────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy repository ──────────────────────────────────────────
COPY . .

# ── Install local randominfo package ────────────────────────
RUN pip install --no-cache-dir -e lesson_17/randominfo-master

# ── Run tests and generate Allure report ────────────────────
CMD ["pytest", "lesson_12/", "lesson_14/", "-v", \
     "--alluredir=allure-results"]