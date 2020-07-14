           git clone https://github.com/frappe/frappe_docker.git
           cd frappe_docker
           cd .devcontainer
           docker-compose --project-name library up -d 
           docker exec  library_frappe_1 sudo chmod 777 .
           docker exec library_frappe_1 bench init --skip-redis-config-generation --frappe-branch version-12 --python /usr/bin/python3.7 frappe-bench
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench set-mariadb-host mariadb
           docker exec -w /workspace/development/frappe-bench library_frappe_1   bench set-redis-cache-host redis-cache:6379
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench set-redis-queue-host redis-queue:6379
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench set-redis-socketio-host redis-socketio:6379

           docker exec -w /workspace/development/frappe-bench library_frappe_1  sed -i '/redis/d' ./Procfile
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench new-site mysite.localhost --mariadb-root-password 123 --admin-password admin --no-mariadb-socket
  
           
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench get-app  library_management https://github.com/yaacine/Frappe_Tuto.git
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench --site mysite.localhost install-app library_management
           
           echo "################## Enabeling Developer mode  ####################"
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench --site mysite.localhost set-config developer_mode 1 > /dev/null


           echo "##################  Enabeling tests  ####################"
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench --site mysite.localhost set-config allow_tests true > /dev/null


           docker exec library_frappe_1 sudo mkdir /reports
           docker exec library_frappe_1 sudo chmod 777 /reports
           docker exec -w /workspace/development/frappe-bench library_frappe_1  bench run-tests --app library_management 

        docker commit library_frappe_1 ${{ secrets.DOCKERHUB_USER }}/myworking_mibrary_container:${{ github.sha }}

