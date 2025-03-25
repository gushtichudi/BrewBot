printf "Your Token:- "
read TOKEN 

if [[ -z $TOKEN ]]; then
  echo "Please put your token" >&2
  exit 1
fi 

echo ok

case $SHELL in 
  "/usr/bin/zsh")
    echo "export BREWBOT_TOKEN=$TOKEN" >> ~/.zshrc
  ;;
  "/usr/bin/bash")
    echo "export BREWBOT_TOKEN=$TOKEN" >> ~/.bashrc
  ;;
  *)
    echo "We cannot work with this shell. Use bash." >&2
    printf "Message for Brewy only: Are you on Termux? [Y/n] "
    read QUES

    if [[ $QUES == "y" ]]; then
      echo "okay i'll just export it to bash"
      echo "export BREWBOT_TOKEN=$TOKEN" >> ~/.bashrc
    fi
  ;;
esac
