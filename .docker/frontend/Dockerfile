FROM node:21.7-slim

WORKDIR /app

COPY ./frontend/package.json /app/

RUN yarn install

COPY ./frontend /app/

CMD ["yarn", "dev"]