-- Create database
CREATE DATABASE IF NOT EXISTS feminist_women CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE feminist_women;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create articles table
CREATE TABLE IF NOT EXISTS articles (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR(100),
    author VARCHAR(100),
    cover_image VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category (category),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert initial categories
INSERT INTO categories (name, description) VALUES
('Politics', 'Articles about feminist politics, policy, and governance'),
('Culture', 'Articles exploring feminist perspectives on culture, arts, and media'),
('Workplace', 'Articles about gender equality in the workplace and career development'),
('Health', 'Articles on reproductive rights, mental health, and wellness'),
('Education', 'Articles about feminist pedagogy and educational equity'),
('Activism', 'Articles highlighting feminist movements and activist work')
ON DUPLICATE KEY UPDATE description = VALUES(description);

-- Insert sample articles
INSERT INTO articles (title, content, category, author, cover_image) VALUES
('The Future of Feminism: Navigating the Fourth Wave',
'Technology has fundamentally transformed how feminist movements organize, communicate, and create change. From #MeToo to online harassment campaigns, digital spaces have become both battlegrounds and sanctuaries for feminist discourse.

The fourth wave of feminism is characterized by its embrace of intersectionality, recognizing that gender cannot be examined in isolation from race, class, sexuality, and ability. This recognition has enriched feminist theory and expanded the movement coalition-building potential.

Social media has democratized voice, allowing marginalized perspectives that were historically excluded from mainstream media to reach global audiences. A teenager in rural America can now speak directly to activists in Mumbai or Lagos, creating unprecedented transnational solidarity networks.

Yet challenges persist. Online harassment, coordinated disinformation campaigns, and algorithmic bias threaten to replicate offline inequalities in digital spaces. The future of feminism depends on our ability to address these emerging threats while building on the movement hard-won gains.',
'Politics',
'Sarah Chen',
'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=800'),

('Breaking Barriers: Women Leading Tech Innovation',
'The technology industry has historically been male-dominated, but women are increasingly reshaping how we think about innovation, leadership, and product design. From Ada Lovelace to Grace Hopper to contemporary leaders, women have been instrumental in computing evolution.

Today, women-led startups are addressing previously overlooked problems, bringing diverse perspectives to product development, and challenging the assumption that technological innovation is inherently neutral. Research consistently shows that diverse teams produce more creative and profitable solutions.

However, the statistics remain troubling. Women, particularly women of color, remain underrepresented in technical roles and executive positions. The pipeline problem persists, but research increasingly suggests that retention is the core challenge. Workplace culture, pay equity, and accessibility remain critical issues.

The path forward requires systemic change: equitable parental leave policies, transparent promotion criteria, and active measures to counteract bias in hiring and evaluation. Companies that embrace these changes are seeing better outcomes.',
'Workplace',
'Maria Garcia',
'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=800'),

('Reproductive Rights: A Global Perspective',
'Reproductive rights remain one of the most contested terrain in contemporary feminist politics. Access to contraception, abortion, and maternal healthcare varies dramatically across and within countries, reflecting broader power dynamics around gender, race, and class.

The global gag rule, which has been reinstated and rescinded multiple times in recent decades, demonstrates how reproductive rights can become politicized as bargaining chips in broader ideological battles. When governments restrict funding for family planning organizations, it is invariably the most vulnerable populations who suffer.

Intersectional approaches to reproductive justice recognize that access is shaped by multiple factors simultaneously. A wealthy woman in a restrictive state may be able to travel for care; a poor woman cannot. Disability rights activists have long argued that reproductive rights include the right to parent as well as the right to not parent.

The struggle for reproductive autonomy is ultimately about self-determination: who controls decisions about our bodies, our futures, and our families. This fundamental principle continues to animate feminist activism worldwide.',
'Health',
'Dr. Emily Brown',
'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800'),

('Intersectionality 101: Understanding Overlapping Oppressions',
'Kimberle Crenshaw concept of intersectionality has become one of the most influential frameworks in contemporary feminist theory. But what does it actually mean, and why does it matter?

Intersectionality emerged from Black feminist critiques of mainstream feminism tendency to treat woman as a monolithic category. Early feminist movements often centered the experiences of white, middle-class women, leaving women of color and working-class women feeling excluded from the very movement that claimed to represent them.

The core insight of intersectionality is that social categories like race, gender, class, and sexuality do not operate independently. They interact and reinforce each other, creating unique experiences of oppression that cannot be understood by examining any single category in isolation.

For contemporary feminist practice, intersectionality demands more than theoretical acknowledgment. It requires actively centering the voices of those most marginalized, examining how our own biases may replicate oppressive structures, and building coalitions that recognize our shared struggles without erasing our differences.',
'Education',
'James Wilson',
'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=800'),

('The Personal is Political: Rethinking Domestic Labor',
'When feminist activists coined the phrase the personal is political, domestic labor was among the first sites of analysis. Yet despite decades of scholarship and activism, inequities in household labor persist and continue to shape gender relations.

Research consistently shows that women, even those who work full-time outside the home, continue to perform the majority of housework and childcare. This second shift contributes to women exhaustion, career limitations, and poorer mental health outcomes.

The COVID-19 pandemic dramatically illustrated these inequalities as schools and daycares closed, forcing families to navigate work and caregiving simultaneously. Women disproportionately reduced their work hours or left the workforce entirely, potentially undoing decades of career progress.

Addressing domestic labor inequities requires multiple interventions: cultural shifts in how we socialize children about gender roles, policy changes like paid family leave and accessible childcare, and fundamental renegotiation of domestic responsibilities within individual households.',
'Politics',
'Sarah Johnson',
'https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?w=800'),

('Women in Film: Beyond the Bechdel Test',
'The Bechdel Test has become a popular shorthand for measuring gender representation in film. But while useful, it represents only a starting point for understanding gender in media.

Women remain underrepresented both in front of and behind the camera. Female directors, writers, and cinematographers are still the exception rather than the rule, particularly in big-budget productions. This matters not just for representation but for content: films directed by women tell different stories and center different perspectives.

The streaming era has created new opportunities for women filmmakers, with platforms increasingly seeking diverse content. However, the concentration of production in a few major studios means that change remains slow and uneven.

More promising is the independent sector, where women filmmakers have long been active and successful. Documentaries, in particular, have provided a space for women voices and stories to reach audiences.',
'Culture',
'Michelle Torres',
'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800'),

('Climate Justice and Gender: A Critical Connection',
'Climate change does not affect all people equally. Women, particularly women in developing nations, are disproportionately vulnerable to environmental degradation, natural disasters, and resource scarcity. Understanding these connections is essential for effective climate justice.

In many societies, women are primarily responsible for food production, water collection, and household energy. When droughts or floods disrupt these systems, it is women who bear the additional labor of adaptation. Women limited access to land, credit, and technology further compounds their vulnerability.

Yet women are also leading climate solutions at all levels. Indigenous women have long been environmental stewards, and their traditional knowledge is increasingly recognized as essential for conservation. Women entrepreneurs are developing clean energy solutions, and women politicians are championing ambitious climate legislation.

Effective climate policy must be gender-responsive, actively working to reduce inequalities rather than exacerbating them. This means ensuring women participation in climate governance and targeting resources to support women climate adaptation and mitigation efforts.',
'Activism',
'Amara Okafor',
'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800'),

('Sexual Harassment in the Workplace: Progress and Challenges',
'The #MeToo movement sparked a long-overdue reckoning with workplace sexual harassment. Powerful men were held accountable, survivor stories were validated, and organizations were forced to examine their cultures.

Yet significant challenges remain. Research suggests that while reporting has increased, formal complaints have not uniformly translated into meaningful consequences for perpetrators. Legal protections for workers remain uneven, and many workers, particularly those in low-wage, non-traditional, and gig economy jobs, lack effective recourse.

Workplace sexual harassment training has become ubiquitous, but evidence for its effectiveness is mixed at best. Some researchers argue that mandatory training may actually reduce reporting by creating hostile environments for complainants.

More promising approaches focus on changing organizational culture rather than individual behavior: bystander intervention programs, transparent reporting mechanisms, leadership accountability, and fostering environments where respectful conduct is the norm rather than the exception.',
'Workplace',
'Jennifer Martinez',
'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=800');
