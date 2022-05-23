FROM node:alpine
RUN mkdir -p /frontend
WORKDIR /frontend
COPY ./ ./
RUN rm package-lock.json
RUN npm install
RUN npm install --only=dev
RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "start:dev"]