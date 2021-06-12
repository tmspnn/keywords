curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > ./install_rust.sh

sh ./install_rust.sh -y 

source $HOME/.cargo/env

pip install -r requirements.txt

