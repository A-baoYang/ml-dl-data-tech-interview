# CI/CD

- Dev + Ops 的實踐
- Continuous Integration 
- Continuous Delivery (需要人為 approve 部署到正式環境)
- Continuous Deployment (自動部署到 正式環境)

- Source Control
    - commit changes
- Build
    - Run unit tests
- Staging
    - Run integration tests, loading tests
- Production 

---

## CI 
- push code to Github
- run unit tests jobs
- code get packaged (ex: docker image) & stored to a repo (ex: DockerHub image repository)
- pros
    - 更高生產力
    - 更快發現錯誤
    - 更快更新與交付

## CD
- 確保每一次釋出的服務是可被信任的（不會因為人為出錯造成服務信賴度降低）
- Infrastructure-tests(CPU,GPU, memory settings, other server support ) to staging & produciton env 
- Integration tests
- User acceptance tests (UAT) (ex: loading speed)
- pros
    - 流程高度自動化
    - （其他同 CI）

## CI/CD Pipeline

![](https://i.imgur.com/1e2CJS4.png)

![](https://i.imgur.com/CQ5n4Ep.png)