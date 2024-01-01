# Anomaly Drug-Target Interaction Discovery via Link Prediction on Knowledge Graphs

This project explores a simple application of the utilization of Knowledge Graphs (KGs) to model complex interconnected data in the biomedical domain.Knowledge graphs (KGs) are ideally suited for modeling complex, interconnected data in the real world. They encapsulate facts, for instance, <'DrugA', 'inhibits', 'ProteinX'>. Despite the abundance of such facts, many knowledge graphs struggle with the issue of 'missing links'. These gaps can be identified through the application of knowledge graph embedding (KGE) models. These models generate semantically meaningful embedding vectors from the provided KG, enabling the prediction of potential relationships between entities. Utilizing this discovery mechanism in a biomedical KG has numerous applications, including the identification of alternative drugs for existing ones and the discovery of new drug-protein interactions. These findings are particularly valuable for pharmaceutical companies in the development of new drugs or in the repurposing of existing ones.

## Project Overview

In this project, the study will be conducted on various knowledge graph embedding (KGE) models, focusing on their training and evaluation methods. The exploration of both knowledge graphs (KGs) and KGEs will lead to a discussion of the potential strengths and weaknesses of each KGE model, with consideration given to their underlying geometry. The performance of different KGE models on various subgraphs, each characterized by distinct relational patterns, will be observed and experimented with visually by the students. Upon reaching this stage, it will be equipped to train a KGE model on a specified KG and commence the application of KGE models to the project dataset.

The primary focus of the project is to build a Drug-Target Knowledge Graph (KG) from existing drug-target interaction data([Yamanishi](http://web.kuicr.kyoto-u.ac.jp/supp/yoshi/drugtarget/)). For this purpose, the [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer) tool was utilized to convert raw data into a knowledge graph format. This process involved understanding the fundamentals of knowledge graphs, their structure, and specifically crafting suitable RML mappings. The ultimate objective was to use trained Knowledge Graph Embedding (KGE) models to forecast interactions between drugs and a range of targets. The project promotes the exploration of various KGE models and the incorporation of pertinent knowledge to exceed established benchmark performance.

## Related Research Papers

- [Knowledge Graph Embedding for Link Prediction: A Comparative Analysis](https://arxiv.org/abs/2002.00819)
- [Translating Embeddings for Modeling Multi-relational Data](https://proceedings.neurips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html)
- [Supervised prediction of drug–target interactions using bipartite local models](https://academic.oup.com/bioinformatics/article/25/18/2397/197654?login=true)
- [Knowledge Graph Embedding by Translating on Hyperplanes](https://ojs.aaai.org/index.php/AAAI/article/view/8870)
- [Embedding entities and relations for learning and inference in knowledge bases](https://arxiv.org/abs/1412.6575)
- [Complex Embeddings for Simple Link Prediction](https://arxiv.org/abs/1606.06357)
- [RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space](https://arxiv.org/abs/1902.10197)
- [5*E Knowledge Graph Embeddings with Projective Transformations](https://arxiv.org/abs/2006.04986)
- [Negative Sampling in Knowledge Representation Learning: A Mini-Review](https://aircconline.com/csit/abstract/v10n15/csit101519.html)
- [Structure Aware Negative Sampling in Knowledge Graphs](https://arxiv.org/abs/2009.11355)
- [Similarity-based machine learning methods for predicting drug-target interactions: a brief review](https://academic.oup.com/bib/article/15/5/734/2422306?login=true)
- [Drug-Target Interaction Prediction Using Semantic Similarity and Edge Partitioning](https://link.springer.com/chapter/10.1007/978-3-319-11964-9_9)
