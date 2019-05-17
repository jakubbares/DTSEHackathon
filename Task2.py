from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=5,
                                random_state=0)
lda.fit(X)