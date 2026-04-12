<template>
  <div class="about-view">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>关于女权主义</h1>
        <p>理解这场运动，它的历史，以及为什么它在今天如此重要。</p>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="mission">
      <div class="section-container">
        <div class="mission-grid">
          <div class="mission-text">
            <h2>我们的使命</h2>
            <p>
              我们相信性别平等不仅是女性的问题，而是人类的问题。我们的平台旨在教育、启发和赋权
              所有性别的人加入为更公正的世界而奋斗的行列。
            </p>
            <p>
              通过深思熟虑的文章、个人故事和对时事的分析，我们旨在让女权主义思想触手可及。
              我们拥抱交叉性，认识到争取平等的斗争必须考虑到种族、阶级、
              性取向和能力如何与性别交叉重叠。
            </p>
          </div>
          <div class="mission-visual">
            <div class="visual-block"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- What is Feminism -->
    <section class="definition">
      <div class="section-container">
        <h2>什么是女权主义？</h2>
        <blockquote>
          "女权主义是对社会、经济和政治平等的信念。"
        </blockquote>
        <p>
          从本质上讲，女权主义很简单：它认为女性应该享有与男性相同权利和机会。
          但这一信念的应用已经经历了两个多世纪的活动和学术发展。
        </p>
      </div>
    </section>

    <!-- Wave Timeline -->
    <section class="timeline">
      <div class="section-container">
        <h2>运动的历史进程</h2>
        <div class="waves">
          <div class="wave">
            <h3>第一波 (1848-1920)</h3>
            <p>
              专注于法律问题，特别是投票权。1848年的塞内卡福尔斯会议标志着
              美国有组织的妇女权利运动的开始。
            </p>
          </div>
          <div class="wave">
            <h3>第二波 (1960s-1980s)</h3>
            <p>
              将斗争扩展到工作场所平等、生殖权利和家庭暴力意识。
              引入了性别作为社会建构的概念。
            </p>
          </div>
          <div class="wave">
            <h3>第三波 (1990s-2000s)</h3>
            <p>
              拥抱多样性和个人能动性。专注于交叉性、
              身体自主性以及挑战对女性气质的狭隘定义。
            </p>
          </div>
          <div class="wave">
            <h3>第四波 (2010s至今)</h3>
            <p>
              以社交媒体为放大器，专注于性骚扰、同意文化和在线行动主义。
              比以往任何时候都更加全球化和包容。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Principles -->
    <section class="principles">
      <div class="section-container">
        <h2>核心原则</h2>
        <div class="principles-grid">
          <div class="principle">
            <div class="principle-icon">01</div>
            <h3>平等</h3>
            <p>
              所有人，无论性别，都应享有平等的权利和机会。
            </p>
          </div>
          <div class="principle">
            <div class="principle-icon">02</div>
            <h3>交叉性</h3>
            <p>
              认识到性别与种族、阶级、性取向以及
              其他形式的身份认同和压迫相互交叉重叠。
            </p>
          </div>
          <div class="principle">
            <div class="principle-icon">03</div>
            <h3>身体自主</h3>
            <p>
              每个人都有权控制自己的身体，包括生殖选择。
            </p>
          </div>
          <div class="principle">
            <div class="principle-icon">04</div>
            <h3>安全</h3>
            <p>
              每个人都应该生活在免受暴力、骚扰和歧视的环境中。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta">
      <div class="cta-content">
        <h2>加入对话</h2>
        <p>阅读我们的文章，成为这场运动的一部分。</p>
        <router-link to="/articles" class="btn-primary">浏览文章</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.about-view {
  padding-top: 48px;
}

.hero {
  padding: 100px 48px 80px;
  text-align: center;
  background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
}

.hero h1 {
  font-size: clamp(48px, 8vw, 72px);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-black);
  margin: 0 0 16px;
}

.hero p {
  font-size: 24px;
  color: var(--color-gray);
  margin: 0;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 48px;
}

/* Mission */
.mission {
  padding: 100px 0;
}

.mission-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.mission-text h2 {
  font-size: 40px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-black);
  margin: 0 0 24px;
}

.mission-text p {
  font-size: 19px;
  line-height: 1.7;
  color: var(--color-gray);
  margin: 0 0 20px;
}

.mission-visual {
  display: flex;
  justify-content: center;
}

.visual-block {
  width: 100%;
  max-width: 400px;
  aspect-ratio: 1;
  background: linear-gradient(135deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 24px;
}

/* Definition */
.definition {
  padding: 100px 0;
  background: #f5f5f7;
  text-align: center;
}

.definition h2 {
  font-size: 40px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-black);
  margin: 0 0 40px;
}

.definition blockquote {
  font-size: clamp(24px, 4vw, 32px);
  font-weight: 600;
  line-height: 1.4;
  color: var(--color-black);
  max-width: 800px;
  margin: 0 auto 40px;
  padding: 0;
  border: none;
}

.definition p {
  font-size: 19px;
  line-height: 1.7;
  color: var(--color-gray);
  max-width: 700px;
  margin: 0 auto;
}

/* Timeline */
.timeline {
  padding: 100px 0;
}

.timeline h2 {
  font-size: 40px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-black);
  margin: 0 0 60px;
  text-align: center;
}

.waves {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 40px;
}

.wave {
  padding: 40px;
  background: #f5f5f7;
  border-radius: 16px;
}

.wave h3 {
  font-size: 21px;
  font-weight: 600;
  color: var(--color-black);
  margin: 0 0 16px;
}

.wave p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--color-gray);
  margin: 0;
}

/* Principles */
.principles {
  padding: 100px 0;
  background: var(--color-black);
}

.principles h2 {
  font-size: 40px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-white);
  margin: 0 0 60px;
  text-align: center;
}

.principles-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 40px;
}

.principle {
  text-align: center;
}

.principle-icon {
  font-size: 48px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.2);
  margin-bottom: 16px;
}

.principle h3 {
  font-size: 21px;
  font-weight: 600;
  color: var(--color-white);
  margin: 0 0 12px;
}

.principle p {
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  margin: 0;
}

/* CTA */
.cta {
  padding: 120px 48px;
  text-align: center;
  background: linear-gradient(180deg, #ffffff 0%, #f5f5f7 100%);
}

.cta-content {
  max-width: 600px;
  margin: 0 auto;
}

.cta h2 {
  font-size: 48px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-black);
  margin: 0 0 16px;
}

.cta p {
  font-size: 19px;
  color: var(--color-gray);
  margin: 0 0 32px;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 16px 32px;
  font-size: 17px;
  font-weight: 500;
  text-decoration: none;
  background: var(--color-black);
  color: var(--color-white);
  border-radius: 980px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: #1d1d1f;
  transform: scale(1.02);
}

@media (max-width: 1024px) {
  .principles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 80px 24px 60px;
  }

  .section-container {
    padding: 0 24px;
  }

  .mission {
    padding: 60px 0;
  }

  .mission-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .visual-block {
    max-width: 280px;
  }

  .definition,
  .timeline,
  .principles {
    padding: 60px 0;
  }

  .waves {
    grid-template-columns: 1fr;
  }

  .principles-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .cta {
    padding: 80px 24px;
  }

  .cta h2 {
    font-size: 36px;
  }
}
</style>