import matplotlib.pyplot as plt


def plot_loss_history(loss_history, output_dir):
    plt.plot(loss_history.history["loss"])
    plt.plot(loss_history.history["val_loss"])
    plt.title("model loss")
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.savefig(open(str(output_dir.joinpath("history.png")),'wb'))
