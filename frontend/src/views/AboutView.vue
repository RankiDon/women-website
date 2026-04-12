<template>
  <div class="about-view">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>About Feminism</h1>
        <p>Understanding the movement, its history, and why it matters today.</p>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="mission">
      <div class="section-container">
        <div class="mission-grid">
          <div class="mission-text">
            <h2>Our Mission</h2>
            <p>
              We believe that gender equality is not just a women's issue—it's a
              human issue. Our platform exists to educate, inspire, and empower
              people of all genders to join the fight for a more just world.
            </p>
            <p>
              Through thoughtful articles, personal stories, and analysis of
              current events, we aim to make feminist ideas accessible to
              everyone. We embrace intersectionality, recognizing that the
              struggle for equality must account for the ways race, class,
              sexuality, and ability intersect with gender.
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
        <h2>What is Feminism?</h2>
        <blockquote>
          "Feminism is the belief in the social, economic, and political equality
          of the sexes."
        </blockquote>
        <p>
          At its core, feminism is simple: it's the belief that women deserve the
          same rights and opportunities as men. But the application of that belief
          has evolved over more than two centuries of activism and scholarship.
        </p>
      </div>
    </section>

    <!-- Wave Timeline -->
    <section class="timeline">
      <div class="section-container">
        <h2>The Movement Through Time</h2>
        <div class="waves">
          <div class="wave">
            <h3>First Wave (1848-1920)</h3>
            <p>
              Focused on legal issues, particularly the right to vote. The Seneca
              Falls Convention in 1848 marked the beginning of the organized women's
              rights movement in America.
            </p>
          </div>
          <div class="wave">
            <h3>Second Wave (1960s-1980s)</h3>
            <p>
              Expanded the fight to workplace equality, reproductive rights, and
              domestic violence awareness. Introduced the concept of gender as a
              social construct.
            </p>
          </div>
          <div class="wave">
            <h3>Third Wave (1990s-2000s)</h3>
            <p>
              Embraced diversity and individual agency. Focused on intersectionality,
              body autonomy, and challenging narrow definitions of femininity.
            </p>
          </div>
          <div class="wave">
            <h3>Fourth Wave (2010s-Present)</h3>
            <p>
              Amplified by social media, focusing on sexual harassment, consent
              culture, and online activism. Global and more inclusive than ever before.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Principles -->
    <section class="principles">
      <div class="section-container">
        <h2>Core Principles</h2>
        <div class="principles-grid">
          <div class="principle">
            <div class="principle-icon">01</div>
            <h3>Equality</h3>
            <p>
              All people deserve equal rights and opportunities, regardless of gender.
            </p>
          </div>
          <div class="principle">
            <div class="principle-icon">02</div>
            <h3>Intersectionality</h3>
            <p>
              Recognizing that gender intersects with race, class, sexuality, and
              other forms of identity and oppression.
            </p>
          </div>
          <div class="principle">
            <div class="principle-icon">03</div>
            <h3>Body Autonomy</h3>
            <p>
              Every person has the right to control their own body, including
              reproductive choices.
            </p>
          </div>
          <div class="principle">
            <div class="principle-icon">04</div>
            <h3>Safety</h3>
            <p>
              Everyone deserves to live free from violence, harassment, and
              discrimination.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta">
      <div class="cta-content">
        <h2>Join the Conversation</h2>
        <p>Read our articles and become part of the movement.</p>
        <router-link to="/articles" class="btn-primary">Explore Articles</router-link>
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