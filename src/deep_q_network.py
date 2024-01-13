{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e0d6e698",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "@author: Viet Nguyen <nhviet1009@gmail.com>\n",
    "\"\"\"\n",
    "import torch.nn as nn\n",
    "\n",
    "class DeepQNetwork(nn.Module):\n",
    "    def __init__(self):\n",
    "        super(DeepQNetwork, self).__init__()\n",
    "\n",
    "        self.conv1 = nn.Sequential(nn.Conv2d(4, 32, kernel_size=8, stride=4), nn.ReLU(inplace=True))\n",
    "        self.conv2 = nn.Sequential(nn.Conv2d(32, 64, kernel_size=4, stride=2), nn.ReLU(inplace=True))\n",
    "        self.conv3 = nn.Sequential(nn.Conv2d(64, 64, kernel_size=3, stride=1), nn.ReLU(inplace=True))\n",
    "\n",
    "        self.fc1 = nn.Sequential(nn.Linear(7 * 7 * 64, 512), nn.ReLU(inplace=True))\n",
    "        self.fc2 = nn.Linear(512, 2)\n",
    "        self._create_weights()\n",
    "\n",
    "    def _create_weights(self):\n",
    "        for m in self.modules():\n",
    "            if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):\n",
    "                nn.init.uniform_(m.weight, -0.01, 0.01)\n",
    "                nn.init.constant_(m.bias, 0)\n",
    "\n",
    "    def forward(self, input):\n",
    "        output = self.conv1(input)\n",
    "        output = self.conv2(output)\n",
    "        output = self.conv3(output)\n",
    "        output = output.view(output.size(0), -1)\n",
    "        output = self.fc1(output)\n",
    "        output = self.fc2(output)\n",
    "\n",
    "        return output\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e282e2e4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "458d83ac",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
