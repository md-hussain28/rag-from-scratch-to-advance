 
Folder strucrture
 
 rag-system/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── constants.py
│   │
│   ├── ingestion/
│   │   ├── loaders/
│   │   │   ├── pdf_loader.py
│   │   │   ├── docx_loader.py
│   │   │   ├── html_loader.py
│   │   │   ├── markdown_loader.py
│   │   │   └── json_loader.py
│   │   │
│   │   ├── parsers/
│   │   │   ├── layout_parser.py
│   │   │   ├── table_parser.py
│   │   │   └── metadata_parser.py
│   │   │
│   │   ├── cleaners/
│   │   │   ├── text_cleaner.py
│   │   │   ├── unicode_cleaner.py
│   │   │   └── deduplicator.py
│   │   │
│   │   └── pipeline.py
│   │
│   ├── chunking/
│   │   ├── fixed_chunker.py
│   │   ├── recursive_chunker.py
│   │   ├── semantic_chunker.py
│   │   ├── token_chunker.py
│   │   └── chunk_utils.py
│   │
│   ├── embeddings/
│   │   ├── embedding_model.py
│   │   ├── embedding_cache.py
│   │   ├── batching.py
│   │   └── vector_normalizer.py
│   │
│   ├── vectorstore/
│   │   ├── faiss_index.py
│   │   ├── metadata_store.py
│   │   ├── persistence.py
│   │   └── vector_utils.py
│   │
│   ├── retrieval/
│   │   ├── dense_retriever.py
│   │   ├── sparse_retriever.py
│   │   ├── hybrid_retriever.py
│   │   ├── metadata_filter.py
│   │   └── query_expansion.py
│   │
│   ├── reranking/
│   │   ├── cross_encoder.py
│   │   ├── rerank_pipeline.py
│   │   └── score_fusion.py
│   │
│   ├── context/
│   │   ├── deduplication.py
│   │   ├── context_builder.py
│   │   ├── token_budget.py
│   │   ├── context_ordering.py
│   │   └── citation_builder.py
│   │
│   ├── prompting/
│   │   ├── system_prompt.py
│   │   ├── prompt_builder.py
│   │   └── templates.py
│   │
│   ├── generation/
│   │   ├── llm_client.py
│   │   ├── response_parser.py
│   │   └── streaming.py
│   │
│   ├── evaluation/
│   │   ├── retrieval_metrics.py
│   │   ├── generation_metrics.py
│   │   ├── benchmark.py
│   │   └── datasets.py
│   │
│   ├── observability/
│   │   ├── logger.py
│   │   ├── tracing.py
│   │   ├── latency.py
│   │   └── token_usage.py
│   │
│   ├── utils/
│   │   ├── tokenizer.py
│   │   ├── hashing.py
│   │   ├── file_utils.py
│   │   └── async_utils.py
│   │
│   └── api/
│       ├── routes.py
│       ├── schemas.py
│       └── server.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── chunks/
│   ├── embeddings/
│   └── indexes/
│
├── notebooks/
│
├── tests/
│
├── requirements.txt
│
└── README.md