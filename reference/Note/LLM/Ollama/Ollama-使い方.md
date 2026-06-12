---
date: 2026-06-13T00:00:00.000Z
description: "headroom MCPのOllama統合設定メモ — OLLAMA_MODEL/OLLAMA_ENDPOINT環境変数・headroom proxy起動手順"
tags:
  - reference
  - ollama
  - local-llm
  - headroom
---

uv run headroom proxy --port 8787

ykomi:~/repo/svn-toppers-TECS-2/git-svn-trunk-tags/tecscde (main) $ uv pip list --system
Using Python 3.13.11 environment at: /home/ykomi/.local/share/mise/installs/python/3.13.11

OLLAMA_MODEL 
OLLAMA_ENDPOINT

===========================
● OLLAMA_MODEL の使い方まとめ：

  設定方法

  この headroom パッケージ（max CLIツール）はOllamaをLLMプロバイダーとして使う場合、以下の2つの環境変数が両方とも必要です。

  設定ファイルの場所: ~/.config/headroom/.env（ユーザー設定ディレクトリ）

  LLM_PROVIDER=ollama
  OLLAMA_MODEL=llama3
  OLLAMA_ENDPOINT=http://localhost:11434

  初回セットアップ

  初回は対話式セットアップを使う方が簡単です：

  uvx --from headroom max

  起動後、CLIで config と入力するとプロバイダーを選択・再設定できます。

  各プロバイダーの対応環境変数

  ┌──────────────┬────────────────────────────────┐
  │ プロバイダー │            環境変数            │
  ├──────────────┼────────────────────────────────┤
  │ ollama       │ OLLAMA_MODEL + OLLAMA_ENDPOINT │
  ├──────────────┼────────────────────────────────┤
  │ openai       │ OPENAI_API_KEY                 │
  ├──────────────┼────────────────────────────────┤
  │ anthropic    │ ANTHROPIC_API_KEY              │
  ├──────────────┼────────────────────────────────┤
  │ google       │ GOOGLE_API_KEY                 │
  ├──────────────┼────────────────────────────────┤
  │ local_gguf   │ LOCAL_GGUF_MODEL_PATH          │
  └──────────────┴────────────────────────────────┘

  例

  LLM_PROVIDER=ollama
  OLLAMA_MODEL=llama3.2
  OLLAMA_ENDPOINT=http://localhost:11434

  Ollamaが localhost:11434 で動いていれば、その後 uvx --from headroom max で起動できます。


===========================================
ykomi:~/repo/github-ai/agentmemory (main=) $ docker-compose -f docker-compose.yml up
[+] up 27/27
 ✔ Image iiidev/iii:0.11.2            Pulled                                                                                                   4.7s
 ✔ Image busybox:1.36                 Pulled                                                                                                   5.2s
 ✔ Network agentmemory_default        Created                                                                                                  0.0s
 ✔ Volume agentmemory_iii-data        Created                                                                                                  0.0s
 ✔ Container agentmemory-iii-init-1   Created                                                                                                  0.3s
 ✔ Container agentmemory-iii-engine-1 Created                                                                                                  0.0s
Attaching to iii-engine-1, iii-init-1
Container agentmemory-iii-init-1 Waiting
iii-init-1 exited with code 0
Container agentmemory-iii-init-1 Exited
iii-engine-1  | Initializing logging from config file: /app/config.yaml
iii-engine-1  | Parsed config file: /app/config.yaml
iii-engine-1  | Log level from config: info, Log format: default, OTel enabled: true
iii-engine-1  | OpenTelemetry initialized: exporter=memory (max_spans=1000), service_name=agentmemory, sampling_ratio=0.1
iii-engine-1  | [07:20:12.967 AM] [INFO] opentelemetry Global meter provider is set. Meters can now be created using global::meter() or global::meter_with_scope().
i
===========================================
ykomi:~/repo/github-ai/headroom (my) $ docker-compose -f docker-compose.yml up
[+] up 18/18
 ✔ Image neo4j:5.26            Pulled                                                                                                         16.1s
 ✔ Image qdrant/qdrant:v1.17.1 Pulled                                                                                                          9.1s
[+] Building 129.2s (24/24) FINISHED
 => [internal] load local bake definitions                                                                                                    0.0s
 => => reading from stdin 556B                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                          0.0s
 => => transferring dockerfile: 4.53kB                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.13-slim                                                                           1.9s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                 0.0s
 => [internal] load .dockerignore                                                                                                             0.0s
 => => transferring context: 893B                                                                                                             0.0s
 => [internal] load build context                                                                                                             0.1s
 => => transferring context: 10.98MB                                                                                                          0.1s
 => [builder  1/11] FROM docker.io/library/python:3.13-slim@sha256:b04b5d7233d2ad9c379e22ea8927cd1378cd15c60d4ef876c065b25ea8fb3bf3           1.4s
 => => resolve docker.io/library/python:3.13-slim@sha256:b04b5d7233d2ad9c379e22ea8927cd1378cd15c60d4ef876c065b25ea8fb3bf3                     0.0s
 => => sha256:e4f4b0eb5b0dcc71159795f3bcefadea9394f9bd56105f769cb0a33119057250 250B / 250B                                                    0.2s
 => => sha256:f3b83f2d9173c5c97086327efdd961d46c8dd661b391fa56c7445ca8c34f1660 11.82MB / 11.82MB                                              1.2s
 => => sha256:db744c23eac55bf8d5cd5fce3abb1457a52434c36e5743e1a330b650f28284e5 1.29MB / 1.29MB                                                0.8s
 => => extracting sha256:db744c23eac55bf8d5cd5fce3abb1457a52434c36e5743e1a330b650f28284e5                                                     0.0s
 => => extracting sha256:f3b83f2d9173c5c97086327efdd961d46c8dd661b391fa56c7445ca8c34f1660                                                     0.1s
 => => extracting sha256:e4f4b0eb5b0dcc71159795f3bcefadea9394f9bd56105f769cb0a33119057250                                                     0.0s
 => [runtime-slim-base 2/6] RUN apt-get update &&     apt-get install -y --no-install-recommends curl &&     rm -rf /var/lib/apt/lists/*      4.8s
 => [builder  2/11] RUN apt-get update &&   apt-get install -y --no-install-recommends     build-essential     g++     curl     ca-certific  12.2s
 => [builder  3/11] RUN python -m pip install --no-cache-dir uv==0.11.18                                                                     14.7s
 => [builder  4/11] RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs       | sh -s -- -y --no-modify-path --profile minimal -c  12.1s
 => [builder  5/11] WORKDIR /build                                                                                                            0.0s
 => [builder  6/11] COPY pyproject.toml uv.lock README.md ./                                                                                  0.0s
 => [builder  7/11] COPY Cargo.toml Cargo.lock rust-toolchain.toml ./                                                                         0.0s
 => [builder  8/11] COPY crates/ crates/                                                                                                      0.0s
 => [builder  9/11] COPY headroom/ headroom/                                                                                                  0.0s
 => [builder 10/11] RUN --mount=type=cache,target=/root/.cache/uv     --mount=type=cache,target=/root/.cargo/registry     --mount=type=cach  76.4s
 => [builder 11/11] RUN cd /tmp && python -c "from headroom._core import DiffCompressor, SmartCrusher;     print(f'build-stage rust core ver  0.4s
 => [runtime-slim-base 3/6] COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages               0.8s
 => [runtime-slim-base 4/6] COPY --from=builder /usr/local/bin/headroom /usr/local/bin/headroom                                               0.1s
 => [runtime-slim-base 5/6] RUN mkdir -p /home/nonroot /data &&     if [ "nonroot" = "nonroot" ]; then       groupadd --gid 1000 nonroot &&   0.2s
 => [runtime-slim-base 6/6] WORKDIR /home/nonroot                                                                                             0.0s
 => exporting to image                                                                                                                        7.8s
 => => exporting layers                                                                                                                       6.4s
 => => exporting manifest sha256:9bbbaf93482fadcabd9cc0a5b9ed43095927ea07c4a0466fc897fafb29f8930f                                             0.0s
 => => exporting config sha256:8c7a0532c25fa63361b93c550f10ac38e3458e3bfb1782d04cf14dcad56b87ed                                               0.0s
 => => exporting attestation manifest sha256:0787eae3dc10a9d62ef78e9114f62d503457705b1e030f2aa0bd152231422641                                 0.0s
 => => exporting manifest list sha256:32ece41aa5b39626f32526247a468816bd7a01b6a876c5d5f6d3dfff82b88def                                        0.0s
[+] up 25/25g to docker.io/library/headroom-headroom-proxy:latest                                                                             0.0s
 ✔ Image neo4j:5.26                    Pulled                                                                                                 16.1s
 ✔ Image qdrant/qdrant:v1.17.1         Pulled                                                                                                  9.1s
 ✔ Image headroom-headroom-proxy       Built                                                                                                 119.2s
 ✔ Network headroom_default            Created                                                                                                 0.0s
 ✔ Volume headroom_qdrant_data         Created                                                                                                 0.0s
 ✔ Volume headroom_neo4j_data          Created                                                                                                 0.0s
 ✔ Container headroom-neo4j-1          Created                                                                                                 0.2s
 ✔ Container headroom-qdrant-1         Created                                                                                                 0.2s
 ✔ Container headroom-headroom-proxy-1 Created                                                                                                 0.0s
Attaching to headroom-proxy-1, neo4j-1, qdrant-1
qdrant-1  |            _                 _
qdrant-1  |   __ _  __| |_ __ __ _ _ __ | |_
qdrant-1  |  / _` |/ _` | '__/ _` | '_ \| __|
qdrant-1  | | (_| | (_| | | | (_| | | | | |_
qdrant-1  |  \__, |\__,_|_|  \__,_|_| |_|\__|
qdrant-1  |     |_|
qdrant-1  |
qdrant-1  | Version: 1.17.1, build: eabee371
qdrant-1  | Access web UI at http://localhost:6333/dashboard
qdrant-1  |
qdrant-1  | 2026-06-09T07:20:34.965706Z  INFO storage::content_manager::consensus::persistent: Initializing new raft state at ./storage/raft_state.json
qdrant-1  | 2026-06-09T07:20:34.982235Z  INFO qdrant: Distributed mode disabled
qdrant-1  | 2026-06-09T07:20:34.982256Z  INFO qdrant: Telemetry reporting enabled, id: 783a431f-361b-4047-ae31-5104f0a170ab
qdrant-1  | 2026-06-09T07:20:34.989195Z  INFO qdrant::actix: REST transport settings: keep_alive=5s, client_request_timeout=5s, client_disconnect_timeout=5s
qdrant-1  | 2026-06-09T07:20:34.989219Z  INFO qdrant::actix: TLS disabled for REST API
qdrant-1  | 2026-06-09T07:20:34.989301Z  INFO qdrant::actix: Qdrant HTTP listening on 6333
qdrant-1  | 2026-06-09T07:20:34.989308Z  INFO actix_server::builder: starting 19 workers
qdrant-1  | 2026-06-09T07:20:34.989312Z  INFO actix_server::server: Actix runtime found; starting in Actix runtime
qdrant-1  | 2026-06-09T07:20:34.989313Z  INFO actix_server::server: starting service: "actix-web-service-0.0.0.0:6333", workers: 19, listening on: 0.0.0.0:6333
qdrant-1  | 2026-06-09T07:20:34.990318Z  INFO qdrant::tonic: Qdrant gRPC listening on 6334
qdrant-1  | 2026-06-09T07:20:34.990329Z  INFO qdrant::tonic: TLS disabled for gRPC API
neo4j-1   | Installing Plugin 'apoc' from /var/lib/neo4j/labs/apoc-*-core.jar to /var/lib/neo4j/plugins/apoc.jar
neo4j-1   | Applying default values for plugin apoc to neo4j.conf
neo4j-1   | Changed password for user 'neo4j'. IMPORTANT: this change will only take effect if performed before the database is started for the first time.
headroom-proxy-1  |
headroom-proxy-1  | ╔═══════════════════════════════════════════════════════════════════════╗
headroom-proxy-1  | ║                         HEADROOM PROXY                                 ║
headroom-proxy-1  | ║           The Context Optimization Layer for LLM Applications          ║
headroom-proxy-1  | ╚═══════════════════════════════════════════════════════════════════════╝
headroom-proxy-1  |
headroom-proxy-1  | Starting proxy server...
headroom-proxy-1  |
headroom-proxy-1  |   URL:          http://0.0.0.0:8787
headroom-proxy-1  |   Mode:         token
headroom-proxy-1  |   Optimization: ENABLED
headroom-proxy-1  |   Caching:      ENABLED
headroom-proxy-1  |   Rate Limit:   ENABLED
headroom-proxy-1  |   Memory:       DISABLED
headroom-proxy-1  |   License:      OSS (no license key)
headroom-proxy-1  |   Code-Aware:   DISABLED (--code-aware or HEADROOM_CODE_AWARE_ENABLED=1 to enable)
headroom-proxy-1  |   Context Tool: rtk
headroom-proxy-1  |   Extensions:   (none discovered)
headroom-proxy-1  |   Telemetry:    ENABLED (anonymous aggregate stats)
headroom-proxy-1  |                 Disable: HEADROOM_TELEMETRY=off or headroom proxy --no-telemetry
headroom-proxy-1  |
headroom-proxy-1  | Routing:
headroom-proxy-1  |   /v1/messages                    → https://api.anthropic.com
headroom-proxy-1  |   /v1/chat/completions            → https://api.openai.com
headroom-proxy-1  |   /v1/responses                   → https://api.openai.com  (HTTP + WebSocket)
headroom-proxy-1  |   /v1internal:streamGenerateContent → https://cloudcode-pa.googleapis.com
headroom-proxy-1  |
headroom-proxy-1  | Usage:
headroom-proxy-1  |   Claude Code:   ANTHROPIC_BASE_URL=http://0.0.0.0:8787 claude
headroom-proxy-1  |   Codex / OpenAI: OPENAI_BASE_URL=http://0.0.0.0:8787/v1 your-app
headroom-proxy-1  |
headroom-proxy-1  | Endpoints:
headroom-proxy-1  |   GET  /livez      Process liveness
headroom-proxy-1  |   GET  /readyz     Traffic readiness
headroom-proxy-1  |   GET  /health     Aggregate health
headroom-proxy-1  |   GET  /stats      Detailed statistics
headroom-proxy-1  |   GET  /stats-history Durable compression history + display session
headroom-proxy-1  |   GET  /metrics    Prometheus metrics
headroom-proxy-1  |
headroom-proxy-1  | Press Ctrl+C to stop.
headroom-proxy-1  |
headroom-proxy-1  | [transformers] PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
neo4j-1           | 2026-06-09 07:20:37.333+0000 INFO  Logging config in use: File '/var/lib/neo4j/conf/user-logs.xml'
neo4j-1           | 2026-06-09 07:20:37.342+0000 INFO  Starting...
neo4j-1           | 2026-06-09 07:20:37.757+0000 INFO  This instance is ServerId{f65fe150} (f65fe150-577e-4939-af18-16164c8dddf8)
neo4j-1           | 2026-06-09 07:20:38.263+0000 INFO  ======== Neo4j 5.26.27 ========
neo4j-1           | 2026-06-09 07:20:40.085+0000 INFO  Anonymous Usage Data is being sent to Neo4j, see https://neo4j.com/docs/usage-data/
neo4j-1           | 2026-06-09 07:20:40.108+0000 INFO  Bolt enabled on 0.0.0.0:7687.
neo4j-1           | 2026-06-09 07:20:40.956+0000 INFO  HTTP enabled on 0.0.0.0:7474.
neo4j-1           | 2026-06-09 07:20:40.957+0000 INFO  Remote interface available at http://localhost:7474/
neo4j-1           | 2026-06-09 07:20:40.960+0000 INFO  id: 2CE07057B8035C18971F0A1FFA1737CB72EC09A1263071A14CB4ACEA14564BF8
neo4j-1           | 2026-06-09 07:20:40.960+0000 INFO  name: system
neo4j-1           | 2026-06-09 07:20:40.960+0000 INFO  creationDate: 2026-06-09T07:20:38.869Z
neo4j-1           | 2026-06-09 07:20:40.960+0000 INFO  Started.
