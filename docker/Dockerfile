FROM node:10-jessie-slim as node
WORKDIR /usr/app/server
COPY ./server .
EXPOSE 3030

CMD ["sh", "-c", "yarn install && yarn start"]

