FROM node:latest

WORKDIR /app
COPY /app/package*.json .
RUN npm install

EXPOSE 5173

COPY /app /app

CMD ["npm", "run", "dev", "--", "--host"]