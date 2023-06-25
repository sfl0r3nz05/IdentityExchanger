FROM node:14.17.0-alpine3.13

# Create app directory
WORKDIR /app
# Install app dependencies A wildcard is used to ensure both package.json AND package-lock.json are copied where available (npm@5+)

# Bundle app source
COPY . .

RUN npm install --legacy-peer-deps

#EXPOSE 8080
CMD ["npm", "start"] 
