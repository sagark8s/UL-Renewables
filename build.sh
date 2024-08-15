hash=$(git rev-parse HEAD)
echo $hash
echo $BUILD_ID

docker_image_name="ul-renewables"

docker build . -t $docker_image_name:$hash
docker tag $docker_image_name:$hash cglensecontainerregistry.azurecr.io/$docker_image_name:$hash
docker tag cglensecontainerregistry.azurecr.io/$docker_image_name:$hash cglensecontainerregistry.azurecr.io/$docker_image_name:$BUILD_ID

echo $D_PASSWORD | docker login cglensecontainerregistry.azurecr.io -u $D_USERNAME --password-stdin
docker push cglensecontainerregistry.azurecr.io/$docker_image_name:$BUILD_ID
#
