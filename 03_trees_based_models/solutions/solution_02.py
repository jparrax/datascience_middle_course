display = DecisionBoundaryDisplay.from_estimator(
    tree, X_train, cmap=plt.cm.RdBu_r, alpha=0.5,
)
_ = data_train.plot.scatter(
    x="Feature #0",
    y="Feature #1",
    c="Classes",
    s=50,
    cmap=plt.cm.RdBu_r,
    ax=display.ax_
)
